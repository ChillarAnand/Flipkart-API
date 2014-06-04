import sys

def main():
    if len(sys.argv) > 1:
        end_point = "http://www.flipkart.com/"
        query = "+".join(sys.argv[1:])
        url = end_point + "search?q=" + query
        print url

    else:
        print "Usage: python Flipkart.py <something to search>"


if __name__ == "__main__":
    main()
