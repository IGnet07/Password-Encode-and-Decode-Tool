<!-- README.md -->

<h1 align="center">Password Encryption and Decryption Tool</h1>

<p align="center">
  <strong>A Python-based command-line tool for securely encrypting and decrypting passwords.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.6%2B-blue" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
</p>

<hr>

<h2>Overview</h2>

<p>This project is a Python-based command-line tool designed to securely encrypt and decrypt passwords using the <code>cryptography</code> library’s <code>Fernet</code> symmetric encryption method. The tool focuses on simplicity and security, offering robust encryption without the overhead of a graphical user interface (GUI).</p>

<h2>Features</h2>

<ul>
  <li><strong>Secure Encryption:</strong> Utilizes the <code>Fernet</code> encryption algorithm to ensure that passwords are encrypted securely and can only be decrypted with the corresponding key.</li>
  <li><strong>Reliable Decryption:</strong> Allows for the decryption of passwords using the same key, ensuring that encrypted data can be reliably accessed when needed.</li>
  <li><strong>Key Generation:</strong> Automatically generates a secure encryption key, which is essential for both encrypting and decrypting passwords.</li>
  <li><strong>Command-Line Interface:</strong> Provides a straightforward command-line interface, making it easy to use and integrate into other scripts or automated workflows.</li>
  <li><strong>Pure Python Implementation:</strong> Written entirely in Python, ensuring readability, ease of modification, and portability.</li>
</ul>

<h2>Requirements</h2>

<ul>
  <li>Python 3.6 or higher</li>
  <li><code>cryptography</code> library (install via pip: <code>pip install cryptography</code>)</li>
</ul>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/yourusername/password-encryption-decryption-tool.git
cd password-encryption-decryption-tool</code></pre>
  </li>
  <li>Install the required library:
    <pre><code>pip install cryptography</code></pre>
  </li>
</ol>

<h2>Usage</h2>

<h3>Generate a Key</h3>
<p>To generate a new encryption key, run the following script:</p>
<pre><code>from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Key: {key.decode()}")</code></pre>

<h3>Encrypt a Password</h3>
<p>To encrypt a password, use the following script:</p>
<pre><code>from cryptography.fernet import Fernet

key = b'your-generated-key-here'  # Replace with your actual key
cipher_suite = Fernet(key)
password = "your-password-here"
encrypted_password = cipher_suite.encrypt(password.encode())
print(f"Encrypted Password: {encrypted_password.decode()}")</code></pre>

<h3>Decrypt a Password</h3>
<p>To decrypt a password, use the following script:</p>
<pre><code>from cryptography.fernet import Fernet

key = b'your-generated-key-here'  # Replace with your actual key
cipher_suite = Fernet(key)
encrypted_password = b'your-encrypted-password-here'  # Replace with your actual encrypted password
decrypted_password = cipher_suite.decrypt(encrypted_password)
print(f"Decrypted Password: {decrypted_password.decode()}")</code></pre>

<h3>Full Example</h3>
<p>Here is a complete example of generating a key, encrypting a password, and decrypting the password:</p>
<pre><code>from cryptography.fernet import Fernet

# Generate and print key
key = Fernet.generate_key()
print(f"Key: {key.decode()}")

# Encrypt password
cipher_suite = Fernet(key)
password = "mySecretPassword"
encrypted_password = cipher_suite.encrypt(password.encode())
print(f"Encrypted Password: {encrypted_password.decode()}")

# Decrypt password
decrypted_password = cipher_suite.decrypt(encrypted_password)
print(f"Decrypted Password: {decrypted_password.decode()}")</code></pre>

<h2>Security Considerations</h2>

<ul>
  <li><strong>Key Storage:</strong> Store the encryption key securely to prevent unauthorized access. Losing the key means losing access to encrypted passwords.</li>
  <li><strong>Secure Environment:</strong> Run the tool in a secure environment to protect against unauthorized access and exposure of sensitive data.</li>
  <li><strong>Updated Dependencies:</strong> Keep the <code>cryptography</code> library up-to-date to ensure the latest security features and patches are applied.</li>
</ul>

<h2>License</h2>

<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contributing</h2>

<p>Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.</p>

<h2>Contact</h2>

<p>For any questions or inquiries, please contact <a href="gaurav.devop@gmail.com">gaurav.devop@gmail.com</a>.</p>
