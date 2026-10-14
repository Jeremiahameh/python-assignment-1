def main():
    file_name = input("Enter the file name: ").lower().strip()
    parts = file_name.split(".")

    if parts[-1] in ("gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"):
        result = f"{parts[0]}/{parts[-1]}"
        print(result)

    else:
        print("Invalid file extension")

main()
