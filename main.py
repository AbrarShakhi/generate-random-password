import get
import generate


if __name__ == "__main__":
    length = get.length(4)
    password = generate.randomly(length)
    print(password)
