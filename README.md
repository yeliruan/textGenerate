# textGenerate
## 基于GAN考虑外部知识和情感属性的文本生成研究


数据预处理 步骤:
---

1. 获取豆瓣电影数据
2. jieba分词 comment.csv和movies文件
3. connection 将comments.csv和movies.csv文件根据电影id连接起来
4. TF-IDF 根据简介和评论的相关性筛选数据样例，数据样例预计筛选5万条，以此更新TF-IDF阈值
5. textRank抽取评论关键词 作为Topic
6. word2vec 将词构建为向量
7. 数据转换为id 中文词语转换成dict中的词语id，以便根据id得到这个词的向量表示
8. 将所有样例的topic去除低频topic后，构建topic集合，以topic.txt保存
9. 简介作为外部知识，长度设置为168，简介词语长度不足168的用'<PAD>'表示，大于168的截取