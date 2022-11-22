import argparse

def get_input_args():
    
    parse = argparse.ArgumentParser()

    parse.add_argument('--dir',type=str,default='pet_images/')
    parse.add_argument('--arch',default='vgg')
    parse.add_argument('--dogfile',default='dognames.txt')

    return parse.parse_args()
