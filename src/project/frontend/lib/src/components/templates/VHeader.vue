<template>
<div id="v-header">
  <p>
    Progress Management App.
  </p>
</div>
</template>

<style scoped lang="scss">
#v-header {
  background-color: $white;
  box-shadow: 0 0 5px $black;
  box-sizing: border-box;
  color: $main-color;
  font-size: 40px;
  font-weight: bold;
  height: 100px;
  line-height: 100px;
  position: fixed; top: 0; left: 0;
  text-align: center;
  width: 100%;
  z-index: 1;
}
</style>

<script>
export default {
  name: "VHeader"
}
</script>