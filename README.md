# Secure Socket Communication with RSA Encryption

This Python script demonstrates secure socket communication between a client and a server using RSA encryption. The communication ensures confidentiality by encrypting messages using RSA public and private keys.

## Prerequisites

- Python 3.x
- The `rsa` library (install using `pip install rsa`)

## Usage

1. Clone or download this repository to your local machine.

2. Open the `main.py` file in a text editor.

3. Modify the following lines in the script to match your setup:

   - Line 18: Replace `<IP ADDRESS>` with the IP address where you want to host the server or connect to.
   - Line 18: Replace `<PORT>` with the desired port number.

   - Line 34: Replace `<IP ADDRESS>` with the IP address of the server you want to connect to.
   - Line 34: Replace `<PORT>` with the port number of the server you want to connect to.

   Note: If you're connecting over the internet, use the public IP address instead of a local one.

4. Open a terminal or command prompt and navigate to the directory containing the script.

5. To host a server, run the script and choose option 1 when prompted. To connect to a server, run the script and choose option 2.

6. Start sending and receiving encrypted messages securely.

## License

This project is licensed under the GNU General Public License (GPL). See the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is for educational purposes only and may not be suitable for production environments. It provides a basic example of secure communication using RSA encryption.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the functionality of this script, feel free to open an issue or submit a pull request.
