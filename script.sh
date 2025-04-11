# Downloads all the files
# The python file then adds the scale component

REPO_OWNER="mojang"
REPO_NAME="bedrock-samples"
FOLDER_PATH="behavior_pack/entities"

mkdir -p "$FOLDER_PATH"
cd "$FOLDER_PATH"

curl -s "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/contents/$FOLDER_PATH" | jq -r '.[] | select(.type=="file") | .download_url' | while read -r url; do
  filename=$(basename "$url")
  curl -L -o "$filename" "$url"
done
