#virtual environment help isolate python dependencies
# use of virtual environment likhna h yaha /.. like how venv help in isolation and freeezing of versions for one particukar project

# v1 - package 1 (pandas)
# v2- package 2 (numpy)
# v3- package 3 (moviepy)

# # Step 1: Install virtualenv globally (optional if using venv)
# pip install virtualenv

# # Step 2: Create a virtual environment named 'env1' using built-in venv
# python -m venv env1
# # or
# python3 -m venv env1

# # Step 3: (Invalid) This command is incorrect – can't execute a folder
# ./env1/    # ❌ Wrong usage

# # Step 4: Navigate into your code/project directories
# cd vault/cpp-practice/apna_college
# cd classwork/D17\ into\ to\ \ 2D\ arr     # Escaping spaces with backslashes
# cd ..                                     # Go one directory up

# # Step 5: Navigate to the bin folder where activation script lives
# cd python-practice/day16/env1/bin

# # Step 6: Activate the virtual environment (macOS/Linux)
# source /Users/debadritapal/Desktop/coding/vault/python-practice/day16/env1/bin/activate

# # Step 7: Install Python libraries inside the virtual environment
# pip install pandas                        # Install pandas
# pip install numpy==1.20.0                 # Install a specific version of numpy
# pip install scipy                         # Install scipy

# # Step 8: Deactivate the virtual environment when you're done
# deactivate

# # Step 9: Check installed packages within the environment
# pip list

# # Step 10: (Optional) Upgrade pip inside the virtual environment
# pip install --upgrade pip