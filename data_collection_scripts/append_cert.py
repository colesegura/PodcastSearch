import ssl
import os
import shutil

# Define the path to the existing certificate file and the new certificate file
existing_cert_file = "/usr/local/lib/python3.8/site-packages/certifi/cacert.pem"
new_cert_file = "C:\\Users\\13342\\source\\repos\\PodcastSearch\\PodcastSearch\\ClientApp\\BaltimoreCyberTrustRoot.crt.pem"

# Create a new file that contains the existing certificate followed by the new certificate
with open(existing_cert_file, 'r') as f:
    existing_certs = f.read()

with open(new_cert_file, 'r') as f:
    new_cert = f.read()

combined_certs = existing_certs + new_cert

with open('combined_certs.pem', 'w') as f:
    f.write(combined_certs)

# Replace the existing certificate file with the new combined certificate file
shutil.copy('combined_certs.pem', existing_cert_file)
