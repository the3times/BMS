
function f1(){
    window.location.reload()
}


$('#btn-logout').click(function () {

    swal({
            title: "确定退出？",
            text: "",     // text: "退出后就不能再使用了",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            closeOnConfirm: false
        },
        function(){

            $.ajax({
                url: '/logout/',
                type: 'get',
                success:function (args) {
                    if (args === 'OK'){
                        swal("退出成功", "", "success");
                        setTimeout(f1, 3000)
                    }else{
                        swal("退出失败", "", "error");
                    }

                }
            });
        });
});