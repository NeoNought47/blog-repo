#!/bin/bash

# 提示用户输入 commit message
read -p "请输入提交信息（commit message）: " msg

# 执行 Git 操作
git add .
git commit -m "$msg"
git push origin main


