<template>
    <div id="app">
        <Bar></Bar>
        <Map></Map>

    </div>
</template>

<script>
  import Bar from './components/Bar.vue'
  import Map from './components/Map.vue'

  export default {
    name: 'App',
    data: function () {
      return {}
    },
    components: {
      Bar,
      Map
    }
  }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>

