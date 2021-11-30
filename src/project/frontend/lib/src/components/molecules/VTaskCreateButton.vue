<template>
<div id="v-task-create-button">
  <form>
    <div class="item">
      <label>
        <p>Task Name</p>
        <div><input type="text" name="task-name"></div>
      </label>
    </div>
    <div class="item">
      <label>
        <p>Duration</p>
        <div><input type="number" name="task-duration"></div>
      </label>
    </div>
    <div class="item">
      <label>
        <p>Deadline</p>
        <div><input type="number" name="task-deadline"></div>
      </label>
    </div>
    <div class="item">
      <button>
        <p>Create</p>
      </button>
    </div>
  </form>
</div>
</template>

<style scoped lang="scss">
.item {
  margin-top: 10px;

  input {
    font-size: 20px;
    height: 50px;
    width: 100%;
  }

  button {
    font-size: 20px;
    height: 50px;
    width: 100%;
  }
}
</style>

<script>
export default {
  name: "VTaskCreateButton"
}
</script>