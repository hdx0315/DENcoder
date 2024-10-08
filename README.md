# DENcoder ![Static Badge](https://img.shields.io/badge/DENcoder-v1-%230f0?logo=python&logoColor=%230f0) ![Static Badge](https://img.shields.io/badge/HirushaDinujaya-hdx0315-%236fffe9?logo=hexo&logoColor=%236fffe9&labelColor=%23000)
## The Decoder & Encoder


DENcoder is a simple desktop application that allows you to encode and decode messages using a user-provided or automatically generated private key. It is built using Python and Tkinter for the GUI.

### The application supports two modes:

- Encode: Converts a plain text message into an encoded format using the provided key.
- Decode: Decodes an encoded message back into its original form using the same key.


### Features
1. Strong Key Generation: A random strong key is generated by default for encoding/decoding.
2. Base64 Encoding: The message is encoded into a safe format that can be easily transmitted or stored.
3. Message History: Keeps track of the last 10 encode/decode operations.
4. GUI Interface: Easy-to-use graphical interface built with Tkinter.


### Installation
#### Prerequisites
- Python 3.x
- The following Python libraries:
    - tkinter (comes bundled with Python)
    - secrets
    - string
    - base64

#### Clone the Repository
First, clone this repository:

```
git clone https://github.com/hdx0315/DENcoder.git
cd DENcoder
```

#### Install Dependencies
> [!TIP]
> No additional dependencies are required beyond standard Python libraries.

#### Running the Application
To run the program, simply execute the Python file:
```
python main.py
```

### How to Use
- Enter a Message: In the "MESSAGE" field, input the message you want to encode or decode.
![Screenshot of GUI.](https://github.com/hdx0315/DENcoder/blob/main/images/ss1.jpg)
- Enter/Generate a Key: You can provide your own key or use the randomly generated key. The key is essential for both encoding and decoding the message.
- Select Mode: Choose whether to Encode or Decode from the drop-down.
- Click "RESULT": The encoded/decoded result will be shown in the result field.
![Screenshot of a Message encode.](https://github.com/hdx0315/DENcoder/blob/main/images/ss2.jpg)
![Screenshot of a Message decode.](https://github.com/hdx0315/DENcoder/blob/main/images/ss3.jpg)
- Check History: A history of the last 10 encoding/decoding operations is displayed in the history panel.
- RESET: Clears all fields and generates a new key.
- EXIT: Closes the application.
Screenshots

### Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are always welcome!

> [!NOTE]
> Fork the repository.
- Create a new branch: git checkout -b my-feature-branch.
- Make your changes and commit: git commit -m 'Add some feature'.
- Push to the branch: git push origin my-feature-branch.
- Open a pull request..

![Static Badge](https://img.shields.io/badge/DENcoder-v1-%230f0?logo=python&logoColor=%230f0)
![Static Badge](https://img.shields.io/badge/HirushaDinujaya-hdx0315-%236fffe9?logo=hexo&logoColor=%236fffe9&labelColor=%23000)

