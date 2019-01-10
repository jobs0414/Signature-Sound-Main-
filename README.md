# ssound-vue

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

For detailed explanation on how things work, consult the [docs for vue-loader](http://vuejs.github.io/vue-loader).

# Vue.js + Django + MaraiaDB 

### Vue.js 파일을 따로 분리해서 webpack을 하는 방법. 
- django db 데이터를 빼올 수가 없음.  이 방법은 좀 더 생각. 

### django 에 Vue.js 코드를 다 넣기.  복잡해지면 Vue.js에 따로 
webpack으로 번들해서 그 파일을 불러 올 것.  
- db을 다 사용할 수 있음. 코드가 컴포넌트 별로 구분이 되는지는 잘 모르겠음. (일단 이 방법으로)  
- python 에 component 별로 vue 체계적으로 하는것이 제일 좋음 

### 기능별로 하나씩 한 사이클 구현을 해가면서 시도하기 
- 회원가입, 코인충전, 등등 

###
기존에 여러 vscode 폴더에 있는 코드들을 하나로 합쳐서 가져오기. 


To do 1/10. 
메인 vue-menu-bar 불러오기 









