<template>
    <div id="detail_wrapper">

    </div>
</template>
<script>
import eventBus from '../event/eventBus';

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
        eventBus.$on('getCompetitions', (data)=>{
            console.log(data);
            this.details = data;
            this.currentDetail = this.details[0];
        });
    },
    watch:{
        competitionIndex(newValue){
            this.currentDetail = this.details[newValue];
        },
        currentDetail(newValue){
            let container = document.getElementById("detail_wrapper");
            let innerHTML = (function(detail){
                let html = '';
                let margin = 5 + 'px';
                let fontWeight = 400;
                let color = "#003569";
                for(let value in detail){
                    if(value === 'homepage' || value === 'img' || value === 'link')
                        continue;
                    html += `<span style="margin-right:${margin}; font-weight:${fontWeight}; color: ${color};">#${detail[value]}</span>`;
                }
                return html;
            })(newValue);

            container.innerHTML = innerHTML;
        }
    }
}
</script>
<style scoped>
#detail_wrapper{
    display: flex;
    flex-direction: column;
}
</style>