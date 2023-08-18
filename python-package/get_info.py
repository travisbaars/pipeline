import toml

# Load pyproject.toml
data = toml.load("pyproject.toml")

# Open INFO file to save version
info = open("INFO", "w")

# Write data to file
# Each entry on a new line
with info as i:
    i.write(data["project"]["name"])
    i.write("\n")
    i.write(data["project"]["version"])

# In pipeline sed can be used to extract this information
# ex.(sed '1!d' INFO) gets the first line of the INFO file