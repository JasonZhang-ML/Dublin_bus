<template>
  <el-row type="flex" justify="center">
    <el-col :span="20">
      <el-form ref="users" :model="users" label-width="small">
        <el-form-item label="username">
          <el-col :span="10">

            <el-input v-model="users.username"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="password">
          <el-col :span="10">
            <el-input v-model="users.password"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item>
          <el-checkbox label="remember me " name="type"></el-checkbox>
        </el-form-item>
        <el-form-item size="large">
          <el-button type="primary">Sign in/Sign up</el-button>
        </el-form-item>
      </el-form>
    </el-col>

  </el-row>
</template>

<script>
export default {
  name: 'UserPage',
  props: {
    users: {
      username: '',
      password: '',
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
