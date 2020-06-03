$('.btn-delete').click(function () {
    let currentBtn = $(this);       // 必须放着这个位置（当前点击的this），不要放在 if(isConfirm)里面了
    swal({
            title: "确定删除?",
            text: "删除后将就找不回来了！",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "确定，删除它",
            cancelButtonText: "算不吧，不删了!",
            closeOnConfirm: false,
            closeOnCancel: false
        },
        function(isConfirm) {
            if (isConfirm) {
                $.ajax({
                    url: currentBtn.attr('delete_url'),
                    type: 'post',
                    data: {'delete_id': currentBtn.attr('delete_id')},
                    success: function (args) {
                        if (args.status_code === 1111){
                            currentBtn.parent().parent().remove();
                            swal("删除成功！", args.msg, "success");
                        }else {
                            swal("删除失败！", args.msg, "error");
                        }
                    }
                });
            } else {
                swal("取消操作", ":)", "error");
            }
        });
});