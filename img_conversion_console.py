import cv2
import argparse

__author__ = 'ibininja'
__version__ = "0.1"
__maintainer__ = "ibininja"


def convert_to_png(image_path, image_name=None, image_destination=None, quality=None, is_show=False, is_verbose=False):
    if is_verbose:
        print "reading image from :", image_path
        if image_destination is None:
            print "destination was not specifying. writing to source"
        
    img = cv2.imread(image_path)
    print "...."
    
    if (image_destination is None):
        print "saving result to :", image_path+"_converted.png"
        cv2.imwrite(image_path+"_converted.png", img, [cv2.IMWRITE_PNG_COMPRESSION,2]) #9 is the quality to output
    else:
        print "saving result to :", image_destination
        cv2.imwrite(image_destination, img, [cv2.IMWRITE_PNG_COMPRESSION,2]) #9 is the quality to output
    print "converstion finished"
    if is_show:
        if is_verbose:
            print "show image now..."
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--impath", help="[Required] path to image")    
    parser.add_argument("-s", "--destination", help="[destination] Optional where to store the image, leave blank to store in same location",required=False)
    parser.add_argument("-w","--showresult", help="[showresult] Optional show a window with the resulted conversion", action="store_true")
    parser.add_argument("-v", "--verbose", help="[verbose] Optional details of result", action="store_true")
    
    args = parser.parse_args()    
    print "commencing conversion"    
    convert_to_png(image_path= args.impath, image_destination=args.destination, is_show=args.showresult, is_verbose=args.verbose)
    print "finished"
    

if __name__=='__main__':
    Main()
