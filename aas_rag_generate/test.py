import json

def main():
    json_text = """{
  "task_count": 2,
  "task_set": [
    {
      "task_number": 1,
      "task_description": "hh 机械手抓起一个小球放到 jj 托盘上",
      "asset_used": [
        {
          "user_description": "hh 机械手"
        },
        {
          "user_description": "小球"
        },
        {
          "user_description": "jj 托盘"
        }
      ]
    },
    {
      "task_number": 2,
      "task_description": "kk 吸盘将小球吸入仓库",
      "asset_used": [
        {
          "user_description": "kk 吸盘"
        },
        {
          "user_description": "小球"
        }
      ]
    }
  ]
}"""
    # 使用 json.loads 将 JSON 字符串转换为 Python 的字典对象
    json_obj = json.loads(json_text)
    print(json_obj)


if __name__ == "__main__":
    main()