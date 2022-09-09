// Handle add like to a msg
$(".add-like").on("click", async function (e) {
  e.preventDefault();
  let msg_id = $(this).attr("id");
  alert("add");
  const new_like = await axios.post(`/users/add_like/${msg_id}`, {
    action: "add",
  });

  if (new_like.data.result == "add_pass") {
    $(this).toggleClass("add-like remove-like");
    $(`.${msg_id}-icon_likes`).toggleClass("fa-heart  fa-thumbs-up");
    $(`#${msg_id}`).toggleClass("btn-primary  btn-secondary");
  }
});

// handle remove like to a msg
$(".remove-like").on("click", async function (e) {
  e.preventDefault();
  alert("remove");
  let msg_id = $(this).attr("id");
  const new_like = await axios.post(`/users/add_like/${msg_id}`, {
    action: "remove",
  });

  if (new_like.data.result == "remove_pass") {
    $(this).toggleClass("remove-like add-like");
    $(`.${msg_id}-icon_likes`).toggleClass("fa-thumbs-up fa-heart");
    $(`#${msg_id}`).toggleClass("btn-secondary btn-primary");
  }
});
