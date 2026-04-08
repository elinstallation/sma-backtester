import kagglehub

kagglehub.login()

path = kagglehub.dataset_download("camnugent/sandp500")

print("Path:", path)