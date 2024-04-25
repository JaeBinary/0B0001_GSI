# 리스트 활용하기

## 리스트 값 추가하기
### append() 메서드
```python
numList = [10, 20, 30]
numList.append(40)          #append() : 리스트 맨 뒤에 요소에 값을 추가!
```
#### 출력결과
    [10, 20, 30, 40]

---
### append() 메서드
```python
numList = [10, 20, 30]
numList.insert(2, 25)       #insert() : 리스트 원하는 번째의 요소에 값을 추가!
```
#### 결과
    [10, 20, 25, 30]
---
<br>

## 리스트 값 삭제하기
### del() 함수
```python
numList = [10, 20, 30]
del(numList[2])             #del() : 리스트 및 리스트 요소 삭제
```
#### 결과
    [10, 20]
---
### remove() 메서드
```python
numList = [10, 20, 30]
numList.remove(10)           #remove() : 리스트 요소의 특정 값 삭제! (중복된 값을 지울 때, 처음 만나는 한 개의 값만 삭제!)
```
#### 결과
    [20, 30]
---
<br>

## 리스트 값 추출
### pop() 메서드
```python
numList = [10, 20, 30]
numList.pop()                 #pop() : 맨 뒤의 값을 추출! (반환을 해준다.)
```
#### 결과
    [30]
---
<br>

## 리스트 값 세기
### count() 메서드
```python
numList = [10, 20, 30]
numList.count(10)             #count() : 리스트에서 찾을 값이 몇 개인지 개수를 세기!
```
### 결과
    1
---
<br>

## 리스트 크기
### len() 함수
```python
numList = [10, 20, 30]
len(numList)                    #len() : 리스트의 크기를 반환!
```
### 결과
    3
---
<br>

## 리스트 값 정렬
### sort() 메서드
```python
numList = [10, 20, 30]
numList.sort()                  #sort() : 리스트의 요소를 정렬! (default : 오름차순)
numList.sort(reverse = True)    #내림차순 정렬!
```
### 결과
    [10, 20, 30]
    [30, 20, 10]
---
<br>

## 리스트 값 반전
### reverse() 메서드
```python
numList = [10, 20, 30]
numList.reverse()                 #reverse() : 리스트의 마지막 인덱스부터 위치가 반전!
```
### 결과
    [30, 20, 10]