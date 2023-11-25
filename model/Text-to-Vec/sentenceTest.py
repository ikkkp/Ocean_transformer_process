from sentence_transformers import CrossEncoder
import urllib3, socket
from urllib3.connection import HTTPConnection


if __name__ == '__main__':
    HTTPConnection.default_socket_options = (
            HTTPConnection.default_socket_options + [
        (socket.SOL_SOCKET, socket.SO_SNDBUF, 2000000),
        (socket.SOL_SOCKET, socket.SO_RCVBUF, 2000000)
    ])
    model = CrossEncoder('vectara/hallucination_evaluation_model')
    scores = model.predict([
        ["A man walks into a bar and buys a drink", "A bloke swigs alcohol at a pub"],
        ["A person on a horse jumps over a broken down airplane.", "A person is at a diner, ordering an omelette."],
        ["A person on a horse jumps over a broken down airplane.", "A person is outdoors, on a horse."],
        ["A boy is jumping on skateboard in the middle of a red bridge.", "The boy skates down the sidewalk on a blue bridge"],
        ["A man with blond-hair, and a brown shirt drinking out of a public water fountain.", "A blond drinking water in public."],
        ["A man with blond-hair, and a brown shirt drinking out of a public water fountain.", "A blond man wearing a brown shirt is reading a book."],
        ["Mark Wahlberg was a fan of Manny.", "Manny was a fan of Mark Wahlberg."],
    ])
    print(scores)
