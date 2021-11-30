<template>
<div id="v-content">
  <div>
    <slot name="content"></slot>
  </div>
</div>
</template>

<style scoped lang="scss">
$header-height: 100px;
// $footer-height: 100px;
#v-content {
  background-color: $white;
  box-sizing: border-box;
  margin-top: $header-height;
  // margin-bottom: $footer-height;
  min-height: 800px;
  padding: 50px;
  position: relative;
  width: 100%;
  z-index: 0;
}
</style>