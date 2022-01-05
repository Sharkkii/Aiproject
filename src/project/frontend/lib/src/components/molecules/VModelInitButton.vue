<template>
<div id="v-model-init-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="items">
      <div class="item">
        <label>
          <p>Model Name</p>
          <div><input type="text" v-model="name"></div>
        </label>
      </div>
      <div class="item">
        <button type="submit">
          <p>Initialize Model</p>
        </button>
      </div>
    </div>
  </form>
</div>
</template>

<style scoped lang="scss">
.items {
  display: flex;
  align-items: flex-end;
  height: 100px;
}

.item {

  width: 50%;

  input {
    box-sizing: border-box;
    font-size: 20px;
    height: 50px;
    width: 100%;
  }

  button {
    box-sizing: border-box;
    font-size: 20px;
    height: 50px;
    width: 100%;
  }
}
</style>

<script>
export default {
  name: "VModelInitButton",
  data: function() {
    return {
      name: ""
    }
  },
  methods: {
    initializeModel: function(data) {
      this.$emit("initialize-model", data);
    },
    submit: function() {
      this.initializeModel({
        name: this.name
      })
    }
  }
}
</script>
