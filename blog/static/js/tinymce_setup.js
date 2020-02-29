tinymce.init({
    //选择textarea区域作为编辑器，也可用class选择器或id选择器作为便器区域，如selector: '.content'
    selector:'textarea',
    //方向从左到右
    directionality:'ltr',
    //mode: "",
    //语言选择中文
    language:'zh_CN',
    //高度为400
    height:400,
    //工具栏上面的补丁按钮
    plugins:['imageupload',
        'advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker',          
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'save table contextmenu directionality emoticons template paste textcolor',            
        'codesample',   
    ],
    //工具栏的补丁按钮
     toolbar:'insertfile undo redo | \
     imageupload | \
     styleselect | \
     bold italic | \
     alignleft aligncenter alignright alignjustify | \
     bullist numlist outdent indent | \
     link image | \
     print preview media fullpage | \
     forecolor backcolor emoticons | \
     codesample fontsizeselect fullscreen',
    //字体大小
    fontsize_formats:'10pt 12pt 14pt 18pt 24pt 36pt',   
    //按tab不换行
    nonbreaking_force_tab:true,
});