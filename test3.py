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

# openai.ChatCompletionとopenai.Imageのコンビネーション

# 1. openai.ChatCompletionで文章を生成する
illust_prompt_jp = '深夜に食べると最高に美味しい食べ物は何ですか？'
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "次の文章に対して、英文で回答してください。回答は必ず1文で完結させてください。"},
        {"role": "user", "content": illust_prompt_jp}
    ]
)
illust_prompt_en = response["choices"][0]["message"]["content"].strip()
print('response: ' + illust_prompt_en)

# 2. openai.Imageでイラストを生成する
response = openai.Image.create(
  prompt=illust_prompt_en,
  n=3,
  size="1024x1024"
)
print(response)