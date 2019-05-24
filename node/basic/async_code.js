function do_db(func){
    setTimeout(()=>{
        func()
    }, 3000)
}

do_db(function() {
    // 数据库操作完毕
    console.log("the sql execute success!");
})

console.log("I love NodeJs.")
