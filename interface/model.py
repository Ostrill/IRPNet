import torch
import pickle
import re


# NN configuration
EMBEDDING_SIZE = 32
HIDDEN_SIZE = 64
OUTPUT_SIZE = 2
RNN_LAYERS = 1
FC_HIDDEN_SIZE = 128

# Parameters paths
TOKEN_DICT_PATH = 'parameters/token_dict.pkl'
MODEL_PATH = 'parameters/model.pt'
EMBEDDING_PATH = 'parameters/embedding.pt'


class Model:

    """Main class of NN model"""

    def __init__(self):
        """Loads all parameters for model"""
        self.embedding = torch.load(EMBEDDING_PATH)
        with open(TOKEN_DICT_PATH, 'rb') as file:
            self.token_dict = pickle.load(file)
        self.tokenizer = re.compile(r'(?:[\w\d]+\-[\w\d]+)|[\w\d]+')
        self.net = IRPNet(embedding=self.embedding,
                          embedding_size=EMBEDDING_SIZE,
                          hidden_size=HIDDEN_SIZE,
                          output_size=OUTPUT_SIZE,
                          fc_hidden_size=FC_HIDDEN_SIZE,
                          rnn_layers=RNN_LAYERS)
        self.net.load_state_dict(torch.load(MODEL_PATH,
                                            map_location=torch.device('cpu')))
        self.net.eval()

    def __review_to_tokens(self, review):
        """Private method for converting text reviews to tokens"""
        return [self.token_dict[token] if token in self.token_dict else 0
                for token in self.tokenizer.findall(review.lower())]

    def process_review(self, review):
        """Returns tuple with positive and negative score of review"""
        reviews_tensor = torch.tensor([(self.__review_to_tokens(review))])

        with torch.no_grad():
            output = self.net(reviews_tensor).view(-1)
        positive, negative = [value.item() for value in output]

        return positive, negative


class IRPNet(torch.nn.Module):

    """NN class working using PyTorch"""

    def __init__(self,
                 embedding,
                 embedding_size,
                 hidden_size,
                 output_size,
                 fc_hidden_size,
                 rnn_layers):
        """Initializes the NN"""
        super().__init__()

        self.hidden_size = hidden_size
        self.rnn_layers = rnn_layers

        self.emb = torch.nn.Embedding.from_pretrained(embedding)

        self.rnn = torch.nn.LSTM(input_size=embedding_size,
                                 hidden_size=hidden_size,
                                 num_layers=rnn_layers,
                                 batch_first=True)

        self.fc1 = torch.nn.Linear(hidden_size, fc_hidden_size)
        self.act1 = torch.nn.Sigmoid()
        self.drop = torch.nn.Dropout(p=0.4)
        self.fc2 = torch.nn.Linear(fc_hidden_size, output_size)
        self.act2 = torch.nn.Softmax(dim=1)

    def forward(self, input_batch):
        """Performs forward propagation in NN"""
        batch_size = input_batch.size()[0]

        input_emb = self.emb(input_batch)
        output, (h, c) = self.rnn(input_emb, (self.init_hidden(batch_size),
                                              self.init_hidden(batch_size)))
        x = h[-1]
        x = self.fc1(x)
        x = self.act1(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.act2(x)

        return x

    def init_hidden(self, batch_size):
        """Returns null-vector for initial state of RNN (c_0 and h_0)"""
        return torch.zeros(self.rnn_layers, batch_size, self.hidden_size,
                           dtype=torch.float)
