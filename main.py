
from config import *
import data
import model

def defineArgs():
    """define args"""
    parser = argparse.ArgumentParser(description = "Chinese_poem_generator.")
    parser.add_argument("-m", "--mode", help = "select mode by 'train' or test or head",
                        choices = ["train", "test", "head"], default = "test")
    return parser.parse_args()

if __name__ == "__main__":
    args = defineArgs()
    trainData = data.POEMS(trainPoems)
    model = model.MODEL(trainData)
    if args.mode == "train":
        model.train()
    else:
        if args.mode == "test":
            poems = model.test()
        else:
            characters = input("please input chinese character:")
            poems = model.testHead(characters)