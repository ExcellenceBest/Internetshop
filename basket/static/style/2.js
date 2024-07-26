<script>
    document.addEventListener("EasyNetShopLoaded", function(event) {
	// Вычисление позиции корзины и анимация перемещения в неё с затуханием
	ens_jQuery(".easynetshop-buy, .btn-ens-action").click(function () {
		var target = ens_jQuery(this);
		var pos = target.offset();
		var cart_pos = ens_jQuery('#enscart_wrapper').offset();
		var clone = target.clone()
			.css({ position: 'absolute', 'z-index': '2100', top: pos.top, left: pos.left })
			.appendTo("body")
			.animate({top: cart_pos.top, left: cart_pos.left, opacity: 0}, 900, function() { clone.remove(); });
		});
	}, false);

document.addEventListener("EasyNetShopModalOpened", function(event) {
	// Отмена показа окна с сообщением о добавлении товара
	if ((ens_jQuery(".easynetshop-modal-addtocart").css('display') != 'none'))
		hideEasynetshopModals();
	}, false);
</script>