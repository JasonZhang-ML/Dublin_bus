<template>
    <div>



        <el-row v-if="beforeLogin" type="flex" justify="center" v-loading.fullscreen.lock="loading">
            <el-col :span="20">
                <el-form ref="users" :model="users" label-width="small">
                    <el-form-item label="username">
                        <!--<el-col :span="10">-->

                        <el-input v-model="users.username"></el-input>
                        <!--</el-col>-->
                    </el-form-item>
                    <el-form-item label="password">
                        <!--<el-col :span="10">-->
                        <el-input type="password" v-model="users.password"></el-input>
                        <!--</el-col>-->
                    </el-form-item>
                    <el-form-item>
                        <el-checkbox label="remember me " name="type"></el-checkbox>
                    </el-form-item>
                    <el-form-item size="large">
                        <el-button type="primary" @click="login">Sign in</el-button>
                        <el-tooltip class="item" effect="dark" content="No worries, get membership now!"
                                    placement="top-end">
                            <el-button type="primary" @click="goSignUp">Sign up</el-button>
                        </el-tooltip>

                    </el-form-item>
                </el-form>
            </el-col>

        </el-row>
        <div v-if="afterLogin">
            <el-row type="flex" justify="center">
                <el-col :span="20">
                    As our valued client, we remove all advertisements for you.
                </el-col>



            </el-row>
            <el-row type="flex" justify="center">
                <el-col :span="20">
                    Let's look forward to more features 😊
                </el-col>



            </el-row>
            <el-row type="flex" justify="center">
                <el-col :span="20">
                    <img class="noAds" src="../assets/NoAds.png" width="50%"/>
                </el-col>



            </el-row>
            <el-row type="flex" justify="center">
                <el-button type="success" @click="signOut">Sign out</el-button>


            </el-row>

        </div>
        <transition name="el-zoom-in-top">
            <div id="register" v-if="signUpPage">
                <el-row type="flex" justify="center">
                    <el-col :span="20">
                        <el-form ref="register" :model="register">
                            <el-form-item label="Username">
                                <el-input v-model="register.username"></el-input>
                            </el-form-item>
                            <el-form-item label="Password">
                                <el-input v-model="register.password" show-password></el-input>
                            </el-form-item>
                            <el-form-item label="Confirm Password">
                                <el-input v-model="register.passwordConfirm" show-password></el-input>
                            </el-form-item>



                            <el-form-item size="large">
                                <el-tooltip class="item" effect="dark" content="Join now!"
                                            placement="top-end">
                                    <el-button type="primary" @click="signUp">Sign up</el-button>
                                </el-tooltip>
                                <el-button type="primary" @click="goPre">Return</el-button>
                            </el-form-item>
                        </el-form>
                    </el-col>
                </el-row>

            </div>
        </transition>

    </div>
</template>

<script>
  import axios from 'axios'

  export default {

    name: 'UserPage',
    data: function () {
      return {
        noAds:"../assets/NoAds.png",//img for NoADs
        loading: false,
        afterLogin: false,
        beforeLogin: true,
        signUpPage: false,
        users: {
          username: '',
          password: '',
        },
        register: {
          username: "",
          password: "",
          passwordConfirm: ""
        }
      }
    },
    methods: {
      // go to sign up page
      goSignUp: function () {
        this.signUpPage = true;
        this.afterLogin = false;
        this.beforeLogin = false;
      },
      goPre:function(){
        this.signUpPage = false;
        this.afterLogin = false;
        this.beforeLogin = true;
      },
//      loading: function () {
//        const loading = this.$loading({
//          lock: true,
//          text: 'Loading',
//          spinner: 'el-icon-loading',
//          background: 'rgba(0, 0, 0, 0.7)'
//        });
//      },
//      注册
      signUp: function () {
        if (this.register.password != this.register.passwordConfirm) {
          this.$notify.error({
            title: 'Sorry',
            message: 'Please enter the same password twice',
            duration: 2000
          });
          return
        }
        this.loading = true
        axios.post('/regist', {
          username: this.register.username,
          password: this.register.password
        }).then(response => {
          this.loading = false
          if (response.data.validation == 1) {
            this.$notify({
              title: 'congratulations',
              message: 'Registered successfully, please Sign in 😊',
              type: 'success',
              duration: 2000
            });
            this.afterLogin = false;
            this.beforeLogin = true;
            this.signUpPage = false;
          }else{
            this.$notify.error({
              title: 'Sorry',
              message: 'This username is occupied, please try another one',
              duration: 2000
            });
            this.register.username=""
          }


        });


      },
      login: function () {
        this.loading = true


        axios.post('/login', {
          username: this.users.username,
          password: this.users.password
        }).then(response => {
          if (response.data.validation == 1) {
            this.$notify({
              title: 'Thanks',
              message: 'Hey! Welcome back 😊',
              type: 'success',
              duration: 2000
            });
            this.afterLogin = true;
            this.beforeLogin = false;
            this.toParent(true)
          } else {
            this.$notify.error({
              title: 'Sorry',
              message: 'Your username or password is not right 😭',
              duration: 2000
            });
            this.users.password=""
          }


        });
        this.loading = false
      },
      signOut: function () {
        this.$notify({
          title: 'Thanks',
          message: 'You are logged out now',
          type: 'success',
          duration: 2000
        });
        this.afterLogin = false;
        this.beforeLogin = true;
//        this.users.username = '';
        this.users.password = '';
        this.toParent(false)
      },
      toParent:function (status) {
        this.$emit("child1",status)
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
