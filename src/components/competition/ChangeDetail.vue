<template>
    <div id="detail_wrapper">

    </div>
</template>
<script>
export default {
    props:['competitionIndex'],
    data(){
        return{
            details: [],
            currentDetail: {},
        }   
    },
    methods:{
    },
    created(){
        //TO-DO back-end 정의 후, json 비동기를 통한 배열 push로 수정할 것
        for(let i = 0; i < 4; i++){
            this.details.push({
                "link" : "홈페이지 링크 문자열"+i,
                "title" : "공모전 제목 문자열"+i,
                "field" : "분야 문자열"+i,
                "target" : "참여 대상 문자열"+i,
                "organization" : "대회 주최 기관 문자열"+i,
                "date" : "날짜 문자열"+i,
                "price" : "총 상금 문자열"+i,
                "won_price" : "우승 상금 문자열"+i,
                "homepage" : "관련 홈페이지 문자열"+i
            });
        }
        this.currentDetail = this.details[0];
    },
    watch:{
        competitionIndex(newValue){
            this.currentDetail = this.details[newValue];
        },
        currentDetail(newValue){
            let container = document.getElementById("detail_wrapper");
            let innerHTML = (function(detail){
                let html = '';
                for(let value in detail){
                    html += '<span style="margin-right:10px">'+ '#' + detail[value] +'</span>';
                }
                return html;
            })(newValue);

            container.innerHTML = innerHTML;
        }
    }
}
</script>
<style scoped>
</style>