# OrganizationとAPI keyを.envから読み込む関数
# 依存ライブラリ: python-dotenv
# .envファイルの中身:
# OPENAI_ORGANIZATION = org-xxxxxxxxxxxxxxxxxxxxxxxx
# OPENAI_API_KEY = sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def get_openai_vars():
    # .envファイルから環境変数を読み込む
    import os
    from dotenv import load_dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    # 環境変数から値を取得する
    organization = os.environ.get("OPENAI_ORGANIZATION_ID")
    api_key = os.environ.get("OPENAI_API_KEY")
    return organization, api_key

# 初期化
import openai
organization, api_key = get_openai_vars()
openai.organization = organization
openai.api_key = api_key

# openai.Imageのテスト
response = openai.Image.create(
  prompt="A portrait of a girl and a cat, vintage illustration from 1980s",
  n=2,
  size="1024x1024"
)
print(response)