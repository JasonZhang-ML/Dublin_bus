<template>
    <div>
        <el-row class="parent_rel" align="middle">
            <el-col :span="1" class="vertically_centered">
                <el-button circle @click="isUserDisplay = true" type="primary" style="margin-left: 0px;">
                    <i class="el-icon-user-solid"></i>
                </el-button>
            </el-col>
            <el-col :span="23" class="vertically_centered">

        <span class="info-right">
             {{ time.nowDate + ' ' + time.nowTime + ' ' + time.nowWeek }}
        <span class="weather">
            <i class="el-icon-heavy-rain"></i>
            20°
        </span>
        </span>
            </el-col>

        </el-row>
        <el-row>
            <el-input placeholder="Your start point"
                      v-model="location.from"
                      suffix-icon="el-icon-edit">
                <template slot="prepend">From:</template>
            </el-input>


        </el-row>
        <el-row>
            <el-input placeholder="Your destination"
                      v-model="location.to"
                      suffix-icon="el-icon-edit">
                <template slot="prepend">_To_ :</template>
            </el-input>

        </el-row>
        <el-row>

            <el-col :span="24">
                <el-button el-button @click="routeSelect = true" type="primary" class="go_button">GO</el-button>
            </el-col>

        </el-row>
        <el-drawer
                title="Join to unlock more functions"
                :visible.sync="isUserDisplay"
                direction="ltr"
                size='300px'
        >
            <UserPage :isUserDisplay="isUserDisplay"></UserPage>
        </el-drawer>

    </div>

</template>

<script>
  import UserPage from "./Userpage.vue"
  export default {
    name: "Bar",
    data() {
      return {
        isUserDisplay: false,
        time: {
          nowDate: "",
          nowTime: "",
          nowWeek: ""
        },
        location: {
          from: '',
          to: ""
        },
      }
    },
    components: {
      UserPage
    },
    methods: {
      currentTime: function () {
        setInterval(this.getDate, 1000);
      },
      getDate: function () {

        var _this = this;
        let yy = new Date().getFullYear();
        let mm = new Date().getMonth() + 1;
        let dd = new Date().getDate();
        let week = new Date().getDay();
        let hh = new Date().getHours();
        let mf =
          new Date().getMinutes() < 10
            ? "0" + new Date().getMinutes()
            : new Date().getMinutes();
        if (week == 1) {
          this.time.nowWeek = "Monday";
        } else if (week == 2) {
          this.time.nowWeek = "Tuesday";
        } else if (week == 3) {
          this.time.nowWeek = "Wednesday";
        } else if (week == 4) {
          this.time.nowWeek = "Thursday";
        } else if (week == 5) {
          this.time.nowWeek = "Friday";
        } else if (week == 6) {
          this.time.nowWeek = "Saturday";
        } else {
          this.time.nowWeek = "Sunday";
        }
        _this.time.nowTime = hh + ":" + mf;
        _this.time.nowDate = yy + "/" + mm + "/" + dd;
      },
    }, mounted() {

      this.currentTime();

    }
  }
</script>
<style scoped>
    @import "../css/style.css";
</style>
