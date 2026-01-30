def print_author():
# Допишите здесь ваш код
author = None

try:
    with open(".env", "r", encoding="utf=8") as file
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue
            if line.startswith("AUTHOR="):
                parts = line.split("=",1)
                if len(parts) == 2:
                    author = parts[1].strip()
                    if (author.startswith('"') and author.endswith('"')) or \
                       (author.startswith("'") and author.endswith("'")):
                        author=parts[1].strip()
                    break 
print(f"Автор проекта: {author}")
