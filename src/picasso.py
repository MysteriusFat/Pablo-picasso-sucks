from artist import Artist
from PIL import Image
import sys
import argparse
import os

def setSize( x, img ):
    aux = float(img.size[0]) / float(x)
    x = int(img.size[1] / aux )
    y = int(img.size[0] / aux )
    return img.resize((y,x))

population = 0
artists = []
generation = 0
output_path = ""
input_path = ""

# run.py -f -p
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True)
    ap.add_argument("-p", "--population", required=True)
    ap.add_argument("-o", "--output_folder", required=False)
    ap.add_argument("-w", "--width" , required = False)

    args = vars(ap.parse_args())

# Set or create output folder
    if args['output_folder'] == None:
        if not 'output' in os.listdir('../'):
            os.mkdir( '../' + 'output', 0755 )
        output_path = '../' + 'output'
    else:
        if not args['output_folder'] in os.listdir('../'):
            print os.listdir('../')
            os.mkdir('../' + args['output_folder'], 0755 )
        output_path = "../" + args['output_folder']

    population = int(args['population'])
    input_path = args['file']

    img = Image.open( input_path )
    if args["width"] != None:
        img = setSize(int(args["width"]), img)
    size = img.size

    artist = Artist(None, 50, size )
    parent_img = artist.draw(size, (0,0,0,255) )
    artist.getFittness(parent_img, img)

    while(1):
        child_artist = Artist(artist.DNA, 50, size)
        child_artist.DNA = child_artist.mutate()
        child_img = child_artist.draw(size,(0,0,0,255))
        child_artist.getFittness(child_img, img)
        artists.append( child_artist )

        for child_artist in artists:
            if child_artist.fittness < artist.fittness:
                artist = child_artist

        if generation % 50 == 0:
            print "[+] Generation: {}".format(generation)
            print "[+] Fittness: {}".format(artist.fittness)
            artist.draw(size,(0,0,0,255), save=True, save_path = output_path, name=str(generation))
        generation += 1
