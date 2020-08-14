<template>

    <div class="stepsBlock">
        <h3 class="stepsBlockTitle">Query Result</h3>
        <el-steps direction="vertical" :active="steps.length-1" align-center finish-status="success">
            <el-step :title="step.way" :description="step.instruction+' '+step.time" v-for="step in steps"
                     :key="step.way"></el-step>

        </el-steps>

    </div>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    components: {},
    methods: {

//
    }, props: {
      steps: {
        type: Array,
        default(){
          return []
        }
      }
    },
    mounted() {
      console.log(this.steps)
    }

  }
</script>
<style scoped>
    @import "../assets/style.css";
</style>