<template>
    <div class="mapBlock">
        <GmapMap
                :center="{lat: 53.3441, lng: -6.26749}"
                :zoom="13"
                map-type-id="terrain"
                style="width: 100%; height: 300px"
                :options="{
   zoomControl: true,
   mapTypeControl: false,
   scaleControl: false,
   streetViewControl: false,
   rotateControl: false,
   fullscreenControl: true,
   disableDefaultUI: false
 }"
        >
        </GmapMap>
    </div>

</template>



<script>
  export default {
    data() {
      return {}
    },
    methods: {

    },
    mounted() {

    },
    components: {},
  }

</script>


