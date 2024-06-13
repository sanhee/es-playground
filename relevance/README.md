# 네이버 웹툰 데이터를 활용해 ES 연관도 검색 스터디

- 연관도
  - 필드 4개 고정 → 제목, 설명, 장르, 작가
  - (TF-IDF) 기본


## 데이터셋
- https://www.kaggle.com/datasets/bmofinnjake/naverwebtoon-datakorean

```
naver.csv

webtoons serialized in Naver Webtoon
id: unique id of the webtoon
title: title of the webtoon
author: writer of the webtoon
genre: genre of the webtoon
description: introduction of the webtoon
rating: average rating out of 10 for the webtoon
date: the most recent update date of the webtoon
completed: completion status
age: the recommended age
free: free service("기다리면 무료") event availablity
link: link of the webtoon
```