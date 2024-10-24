from convert.py import imageToPDF

def main():
    file = input("Please enter your file to convert:")
    try:
        imagetoPDF(file)
    except Exception as e:
        print("error")

if __name__ == "__main__":
    main()

    
