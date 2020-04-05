<?php
/**
 * File that define P24_Multi_Currency class.
 *
 * @package Przelewy24
 */

defined( 'ABSPATH' ) || exit;

/**
 * Class P24_Multi_Currency
 *
 * Add elementary functions to support multi currency.
 */
class P24_Multi_Currency {

	const WP_JSON_GET_KEY_CURRENCY = 'currency';
	const SESSION_ACTIVE_CURRENCY  = 'przelewy24_active_currency';


	// WooCommerce values - no constants are used in WC libraries for them.
	const WOOCOMMERCE_FIELD_DECIMAL_SEPARATOR  = 'decimal_separator';
	const WOOCOMMERCE_FIELD_THOUSAND_SEPARATOR = 'thousand_separator';
	const WOOCOMMERCE_FIELD_DECIMALS           = 'decimals';

	/**
	 * Instance of core of plugin.
	 *
	 * @var P24_Core
	 */
	private $plugin_core;

	/**
	 * The currency to display for users.
	 *
	 * @var string|null
	 */
	private $active_currency;

	/**
	 * P24_Multi_Currency constructor.
	 *
	 * @param P24_Core    $plugin_core Instance of main plugin.
	 * @param string|null $active_currency Active currency to set.
	 */
	public function __construct( P24_Core $plugin_core, $active_currency ) {
		$this->plugin_core     = $plugin_core;
		$this->active_currency = $active_currency;
	}

	/**
	 * Get reports currency.
	 *
	 * @param string|null $default Default reports currency.
	 *
	 * @return string|null
	 */
	public static function get_admin_reports_currency( $default = null ) {
		if ( ! isset( $_COOKIE['admin_p24_reports_currency'] ) ) {
			return $default;
		}

		return sanitize_text_field( wp_unslash( $_COOKIE['admin_p24_reports_currency'] ) );
	}

	/**
	 * Get sql query which filters report data by order currency.
	 *
	 * @param string $order_table Name of table with orders (without prefix).
	 *
	 * @return string
	 */
	public static function get_currency_filter_for_reports( $order_table ) {
		/**
		 * Global variable usage suggested in WordPress Documentation:
		 * https://developer.wordpress.org/reference/classes/wpdb/ .
		 *
		 * Unfortunately there does not seem to be any alternative to access db prefix by global variables.
		 */
		global $wpdb;
		$metadata_table = esc_sql( "{$wpdb->prefix}postmeta" );
		$currency       = esc_sql( self::get_admin_reports_currency( get_woocommerce_currency() ) );
		$metadata_alias = 'p24_postmeta';
		$order_table    = esc_sql( $order_table );

		return " JOIN {$metadata_table} as {$metadata_alias} ON (" .
			"{$metadata_alias}.meta_key = '_order_currency'" . ' AND ' .
			"{$metadata_alias}.meta_value = '" . $currency . "'" . ' AND ' .
			"{$metadata_alias}.post_id = {$order_table}.order_id)";
	}

	/**
	 * Get active currency.
	 *
	 * @return string
	 */
	public function get_active_currency() {
		if ( ! $this->active_currency ) {
			$multipliers = $this->get_multipliers();
			if ( $this->plugin_core->is_in_user_mode() ) {
				$session = WC()->session;
				/* Try load from session. */
				if ( $session ) {
					$this->active_currency = $this->get_active_currency_from_session( $session, $multipliers );
				}
			} elseif ( $this->plugin_core->is_in_json_mode() ) {
				if ( array_key_exists( self::WP_JSON_GET_KEY_CURRENCY, $_GET ) ) {
					$this->active_currency = (string) $_GET[ self::WP_JSON_GET_KEY_CURRENCY ];
				}
			} elseif ( is_admin() ) {
				/* Admin panel. */
				if ( isset( $_COOKIE['admin_p24_currency'] ) ) {
					$this->active_currency = sanitize_text_field( wp_unslash( $_COOKIE['admin_p24_currency'] ) );
				}
			}

			if ( ! $this->active_currency || ! array_key_exists ( $this->active_currency, $multipliers ) ) {
				$this->active_currency = P24_Woo_Commerce_Low_Level_Getter::get_unhooked_currency_form_woocommerce();
			}
		}

		return $this->active_currency;
	}

	/**
	 * Get default currency.
	 *
	 * It may be different from active currency.
	 *
	 * @return string
	 */
	public function get_default_currency() {
		return P24_Woo_Commerce_Low_Level_Getter::get_unhooked_currency_form_woocommerce();
	}

	/**
	 * Save active currency to session.
	 *
	 * The function has to be called after session creation.
	 */
	public function save_currency_to_session() {
		$session = WC()->session;
		if ( $session ) {
			$old_active_currency = $session->get( self::SESSION_ACTIVE_CURRENCY );
			if ( $this->active_currency !== $old_active_currency ) {
				$session->set( self::SESSION_ACTIVE_CURRENCY, $this->active_currency );
			}
		}
	}

	/**
	 * Try to get active currency from session.
	 *
	 * @param WC_Session|WC_Session_Handler $session
	 * @param array $multipliers
	 * @return string|null
	 */
	private function get_active_currency_from_session( $session, array $multipliers )
	{
		$this->active_currency = $session->get( self::SESSION_ACTIVE_CURRENCY );
		if ( ! $this->active_currency || ! array_key_exists( $this->active_currency, $multipliers ) ) {
			/* Fix session. */
			$this->active_currency = P24_Woo_Commerce_Low_Level_Getter::get_unhooked_currency_form_woocommerce();
			$this->save_currency_to_session();
		}

		return $this->active_currency;
	}

	/**
	 * Get array of multipliers for currencies.
	 *
	 * @return array
	 */
	public function get_multipliers() {
		$set             = get_option( 'przelewy24_multi_currency_multipliers', [] );
		$default         = P24_Woo_Commerce_Low_Level_Getter::get_unhooked_currency_form_woocommerce();
		$set[ $default ] = 1;
		return $set;
	}

	/**
	 * Get list of available currencies.
	 *
	 * It is based on multipliers.
	 *
	 * @return array
	 */
	public function get_available_currencies() {
		$set  = $this->get_multipliers();
		$keys = array_keys( $set );
		return array_combine( $keys, $keys );
	}

	/**
	 * Method for filter that change default currency.
	 *
	 * The default value is ignored.
	 * The wrapped function should always return something.
	 *
	 * @param mixed $default Default value provided by filter.
	 * @return string
	 */
	public function try_change_default_currency( $default ) {
		return $this->get_active_currency() ?: $default;
	}

	/**
	 * Try change price format.
	 *
	 * @param mixed  $default Default value.
	 * @param string $option Name of option.
	 * @return mixed
	 */
	private function try_change_price_format( $default, $option ) {
		$is_reports_context = $this->plugin_core->get_context_provider()->is_reports_context();
		/* Do not change defaults on admin panel except for reports. */
		if ( is_admin() && ! $is_reports_context ) {
			return $default;
		}
		$currency = $is_reports_context ? $this->get_admin_reports_currency() : $this->get_active_currency();
		if ( null === $currency ) {
			return $default;
		}
		$format = $this->get_przelewy24_multi_currency_format( $currency, $option );

		return null !== $format ? $format : $default;
	}

	/**
	 * Get price format from multicurrency settings.
	 *
	 * @param string $currency Default value.
	 * @param string $option   Name of option.
	 *
	 * @return string|null
	 */
	private function get_przelewy24_multi_currency_format( $currency, $option ) {
		$formats = get_option( 'przelewy24_multi_currency_formats', array() );
		if ( ! array_key_exists( $currency, $formats ) || ! array_key_exists( $option, $formats[ $currency ] ) ) {
			return null;
		}
		$return = $formats[ $currency ][ $option ];
		if ( 'thousand_separator' !== $option && '' === $return ) {
			return null;
		}

		return $return;
	}

	/**
	 * Try change thousand separator.
	 *
	 * @param string $default Default thousand separator.
	 * @return string
	 */
	public function try_change_thousand_separator( $default ) {
		return $this->try_change_price_format( $default, 'thousand_separator' );
	}

	/**
	 * Try change decimal separator.
	 *
	 * @param string $default Default decimal separator.
	 * @return string
	 */
	public function try_change_decimal_separator( $default ) {
		return $this->try_change_price_format( $default, 'decimal_separator' );
	}

	/**
	 * Try change number of fraction digits.
	 *
	 * @param mixed $default Default number of fraction digits.
	 * @return mixed
	 */
	public function try_change_decimals( $default ) {
		return $this->try_change_price_format( $default, 'decimals' );
	}

	/**
	 * Try change currency position.
	 *
	 * @param string $default Default currency position.
	 * @return string
	 */
	public function try_change_currency_pos( $default ) {
		return $this->try_change_price_format( $default, 'currency_pos' );
	}

	/**
	 * Add scripts used on admin page.
	 */
	public function add_admin_scripts() {
		wp_enqueue_script( 'p24_multi_currency_admin_script', PRZELEWY24_URI . 'assets/js/p24_multi_currency_admin_script.js', [ 'jquery' ], P24_Core::SCRIPTS_VERSION, true );
	}

	/**
	 * Add scripts used on user page.
	 */
	public function add_user_scripts() {
		wp_enqueue_style( 'p24_multi_currency_form', PRZELEWY24_URI . 'assets/css/p24_multi_currency_style.css', [], P24_Core::SCRIPTS_VERSION );
	}

	/**
	 * An AJAX method to change currency for admin.
	 */
	public function admin_ajax_change_currency() {
		header( 'Content-Type: text/plain; charset=utf-8' );
		wc_setcookie( 'admin_p24_currency', $this->get_active_currency() );
		echo 'Ok';
		wp_die();
	}

	/**
	 * Try find name of class for product.
	 *
	 * This method works as filter. The suggested class is required to do proper override.
	 *
	 * @param string $suggested Suggested product class.
	 * @param string $type Product type.
	 * @param string $variation Product variation.
	 * @param int    $product_id Product id.
	 * @return string
	 * @throws LogicException If nothing was provided or found.
	 */
	public function find_product_class( $suggested, $type, $variation, $product_id ) {
		$rx = '/^WC\\_Product\\_(.+)$/';
		if ( preg_match( $rx, $suggested, $m ) ) {
			$class = 'P24_Product_' . $m[1];
		} else {
			$class = $suggested;
		}
		if ( class_exists( $class ) ) {
			return $class;
		} else {
			$msg = "Cannot find class $class, suggested was $suggested, type was $type, variation was $variation, id was $product_id";
			throw new LogicException( $msg );
		}
	}

	/**
	 * Update price hash.
	 *
	 * The multiplier for currency is added.
	 *
	 * @param array      $hash Default hash.
	 * @param WC_Product $product The product.
	 * @param string     $context The context.
	 * @return array
	 * @throws LogicException If the currency is not configured.
	 */
	public function filter_price_hash( $hash, $product, $context ) {
		if ( method_exists( $product, 'get_currency' ) ) {
			$currency    = $product->get_currency( $context );
			$multipliers = $this->get_multipliers();
			if ( ! array_key_exists( $currency, $multipliers ) ) {
				throw new LogicException( "The requested currency $currency is not configured." );
			}
			$hash[] = $multipliers[ $currency ];
		}
		return $hash;
	}

	/**
	 * Try override active currency.
	 *
	 * The communication with Przelewy24 is quite late.
	 *
	 * @param P24_Communication_Parser $parser The P24_Communication_Parser instance.
	 */
	public function try_override_active_currency( P24_Communication_Parser $parser ) {
		if ( $parser->is_valid() ) {
			$this->active_currency = $parser->get_currency();
		}
	}

	/**
	 * Replaces store element.
	 *
	 * @param array $results Current stores.
	 *
	 * @return array
	 */
	public static function add_to_store( $results ) {
		$p24_stores = array(
			'report-orders-stats'    => 'P24_Orders_Stats_Data_Store',
			'report-revenue-stats'   => 'P24_Orders_Stats_Data_Store',
			'report-products-stats'  => 'P24_Products_Stats_Data_Store',
			'report-products'        => 'P24_Products_Data_Store',
			'report-categories'      => 'P24_Categories_Data_Store',
			'report-orders'          => 'P24_Orders_Data_Store',
			'report-variations'      => 'P24_Variations_Data_Store',
			'report-taxes'           => 'P24_Taxes_Data_Store',
			'report-taxes-stats'     => 'P24_Taxes_Stats_Data_Store',
			'report-coupons'         => 'P24_Coupons_Data_Store',
			'report-coupons-stats'   => 'P24_Coupons_Stats_Data_Store',
			'report-customers'       => 'P24_Customers_Data_Store',
			'report-customers-stats' => 'P24_Customers_Stats_Data_Store',
		);

		return array_merge( $results, $p24_stores );
	}

	/**
	 * Compute price in provided currency.
	 *
	 * @param mixed  $price Price in default currency.
	 * @param string $currency Provided currency.
	 * @return mixed
	 * @throws LogicException If currency is not found.
	 */
	public function compute_price_in_currency( $price, $currency ) {
		if ( ! $price ) {
			/* We have to preserve different false values. */
			return $price;
		}
		$multipliers = $this->get_multipliers();
		if ( array_key_exists( $currency, $multipliers ) ) {
			$multiplier = $multipliers[ $currency ];
		} else {
			throw new LogicException( "The currency $currency not found in config." );
		}
		if ( 1.0 === (float) $multiplier ) {
			return $price;
		} else {
			return $price * $multiplier;
		}
	}

	/**
	 * Compute prices for sending package.
	 *
	 * @param array $rates The set of rages.
	 *
	 * @return array
	 */
	public function update_package_rates( $rates ) {
		$currency = $this->get_active_currency();

		$ret = array();
		foreach ( $rates as $idx => $rate ) {
			$cost = $rate->get_cost();
			$cost = $this->compute_price_in_currency( $cost, $currency );
			$rate->set_cost( $cost );

			$taxes          = $rate->get_taxes();
			$currencies_map = array_fill_keys( array_keys( $taxes ), $currency );
			$taxes_keys     = array_keys( $taxes );
			$taxes          = array_map( array( $this, 'compute_price_in_currency' ), $taxes, $currencies_map );
			$rate->set_taxes( array_combine( $taxes_keys, $taxes ) );

			$ret[ $idx ] = $rate;
		}
		return $rates;
	}

	/**
	 * Try override one field for multi currency.
	 *
	 * @param string $field The name of field in meta table.
	 * @param array  $sql The SQL split into few parts.
	 *
	 * @return array
	 */
	private function sql_override_field( $field, $sql ) {
		$rxs = '/^(.*\\S)\\s?SUM\\s*\\(\\s*meta_' . $field . '\\.meta_value\\s*\\)(.*)$/Dis';
		$rxj = '/INNER\\s+JOIN\\s+(\\S*postmeta)\\s+AS\\s+(\\S+)\\s+ON\\s*\\([^\\)]*\\.meta_key\\s*\\=\\s*\\\'' . $field . '\\\'[^\\)]*\\)/is';
		if ( preg_match( $rxs, $sql['select'], $ms ) && preg_match( $rxj, $sql['join'], $mj ) ) {
			$meta_tbl      = $mj[1];
			$base_tbl      = $mj[2];
			$our_tbl       = $base_tbl . '_p24dc';
			$our_field     = $field . '_p24dc';
			$select_head   = $ms[1];
			$select_tail   = $ms[2];
			$sql['select'] = "$select_head SUM(IFNULL($our_tbl.meta_value, $base_tbl.meta_value ) )$select_tail";
			$sql['join']   = $sql['join'] . "\n"
				. " LEFT JOIN $meta_tbl AS $our_tbl ON (\n"
				. " $our_tbl.meta_key = '$our_field'\n"
				. " AND $our_tbl.post_id = $base_tbl.post_id\n"
				. " )\n";
		}
		return $sql;
	}

	/**
	 * Override SQL to be compatible with multi currency.
	 *
	 * @param array $sql The SQL split into few parts.
	 *
	 * @return array
	 */
	public function sql_override( $sql ) {
		if ( array_key_exists( 'select', $sql ) && array_key_exists( 'join', $sql ) ) {
			$sql = $this->sql_override_field( '_order_total', $sql );
			$sql = $this->sql_override_field( '_order_tax', $sql );
			$sql = $this->sql_override_field( '_order_shipping', $sql );
			$sql = $this->sql_override_field( '_order_shipping_tax', $sql );
			$sql = $this->sql_override_field( '_order_discount', $sql );
			$sql = $this->sql_override_field( '_order_discount_tax', $sql );
		}
		return $sql;
	}

	/**
	 * Add additional fields to order.
	 *
	 * @param WC_Abstract_Order $order The order to save.
	 */
	public function before_order_save( $order ) {
		$dc = $this->get_default_currency();
		$oc = $order->get_currency();
		if ( $dc !== $order->get_currency() ) {
			$multipliers     = $this->get_multipliers();
			$multiplier      = $multipliers[ $oc ];
			$total           = $order->get_total();
			$dc_total        = $total / $multiplier;
			$tax             = $order->get_cart_tax();
			$dc_tax          = $tax / $multiplier;
			$shipping        = $order->get_shipping_total();
			$dc_shipping     = $shipping / $multiplier;
			$shipping_tax    = $order->get_shipping_tax();
			$dc_shipping_tax = $shipping_tax / $multiplier;
			$discount        = $order->get_discount_total();
			$dc_discount     = $discount / $multiplier;
			$discount_tax    = $order->get_discount_tax();
			$dc_discount_tax = $discount_tax / $multiplier;
			$order->add_meta_data( '_order_total_p24dc', $dc_total, true );
			$order->add_meta_data( '_order_tax_p24dc', $dc_tax, true );
			$order->add_meta_data( '_order_shipping_p24dc', $dc_shipping, true );
			$order->add_meta_data( '_order_shipping_tax_p24dc', $dc_shipping_tax, true );
			$order->add_meta_data( '_cart_discount_p24dc', $dc_discount, true );
			$order->add_meta_data( '_cart_discount_tax_p24dc', $dc_discount_tax, true );
			if ( $order instanceof WC_Order_Refund ) {
				$refund    = $order->get_amount();
				$dc_refund = $refund / $multiplier;
				$order->add_meta_data( '_refund_amount_p24dc', $dc_refund, true );
			}
		}
	}

	/**
	 * Update order currency.
	 *
	 * The function should be called after nonce verification.
	 * We have to get the raw data from global variable, though.
	 *
	 * @param int|null $id The id of order.
	 */
	public function update_order_currency( $id ) {
		if ( isset( $_POST['p24_order_currency'] ) ) {
			$currency  = sanitize_text_field( wp_unslash( $_POST['p24_order_currency'] ) ); // WPCS: CSRF ok.
			$available = $this->get_available_currencies();
			if ( in_array( $currency, $available, true ) ) {
				update_metadata( 'post', $id, '_order_currency', $currency );
			}
		}
	}

	/**
	 * Register widget for multi currency.
	 */
	public function register_widget() {
		$widget = new P24_Currency_Selector_Widget( $this->plugin_core );
		register_widget( $widget );
	}

	/**
	 * Updates admin report rest controllers.
	 *
	 * @param array $controllers Rest controllers supplied for reports context.
	 *
	 * @return array
	 */
	public function update_admin_rest_controllers( $controllers ) {
		$key = array_search( 'Automattic\WooCommerce\Admin\API\Leaderboards', $controllers, true );
		if ( false === $key ) {
			return $controllers;
		}

		$controllers[ $key ] = 'P24_Leaderboards_Controller';

		return $controllers;
	}

	/**
	 * Update admin wc price format arguments.
	 *
	 * @param array $args Currency arguments.
	 *
	 * @return array
	 */
	public function update_wc_price_format_arguments( $args ) {
		$currency = isset( $args[ self::WP_JSON_GET_KEY_CURRENCY ] ) && $args[ self::WP_JSON_GET_KEY_CURRENCY ]
			? $args[ self::WP_JSON_GET_KEY_CURRENCY ] : get_woocommerce_currency();
		foreach ( self::get_multi_currency_format_fields() as $argument ) {
			$p24_multi_currency_value = $this->get_przelewy24_multi_currency_format( $currency, $argument );
			if ( null !== $p24_multi_currency_value ) {
				$args[ $argument ] = $p24_multi_currency_value;
			}
		}
		$args['price_format'] = $this->get_currency_format_for_currency_pos(
			$this->get_przelewy24_multi_currency_format( $currency, 'currency_pos' )
		);

		return $args;
	}

	/**
	 * Get multi currency format fields.
	 *
	 * @return array
	 */
	public static function get_multi_currency_format_fields() {
		return array(
			self::WOOCOMMERCE_FIELD_DECIMAL_SEPARATOR,
			self::WOOCOMMERCE_FIELD_THOUSAND_SEPARATOR,
			self::WOOCOMMERCE_FIELD_DECIMALS,
		);
	}

	/**
	 * Get currency format from currency position.
	 *
	 * @param string|null $currency_pos Currency position. Allowed values are: left, right, left_space and right_space.
	 *
	 * @return string Value for 'left' will be returned by default - just like in WooCommerce.
	 */
	private function get_currency_format_for_currency_pos( $currency_pos = null ) {
		switch ( $currency_pos ) {
			case 'right':
				return '%2$s%1$s';
			case 'left_space':
				return '%1$s&nbsp;%2$s';
			case 'right_space':
				return '%2$s&nbsp;%1$s';
			default: // left - like in dollars.
				return '%1$s%2$s';
		}
	}

	/**
	 * Bind events to use multi currency.
	 */
	public function bind_events() {
		add_action( 'wp_ajax_p24_change_currency', array( $this, 'admin_ajax_change_currency' ) );
		add_filter( 'przelewy24_multi_currency_options', array( $this, 'get_available_currencies' ) );
		add_action( 'wp_enqueue_scripts', array( $this, 'add_user_scripts' ) );
		add_action( 'admin_enqueue_scripts', array( $this, 'add_admin_scripts' ) );
		add_action( 'widgets_init', array( $this, 'register_widget' ) );

		if ( ! is_admin() ) {
			add_filter( 'woocommerce_currency', array( $this, 'try_change_default_currency' ) );
			add_filter( 'wc_get_price_decimals', array( $this, 'try_change_decimals' ) );
			add_action( 'wp_loaded', array( $this, 'save_currency_to_session' ) );
			add_filter( 'woocommerce_package_rates', array( $this, 'update_package_rates' ) );
		}
		if ( $this->plugin_core->get_context_provider()->is_reports_context() ) {
			add_filter( 'woocommerce_currency', array( $this, 'get_admin_reports_currency' ) );
			add_filter( 'woocommerce_data_stores', array( __CLASS__, 'add_to_store' ) );
		}
		add_filter( 'wc_price_args', array( $this, 'update_wc_price_format_arguments' ) );
		add_filter( 'option_woocommerce_currency_pos', array( $this, 'try_change_currency_pos' ) ); /* Core event. */
		add_filter( 'wc_get_price_thousand_separator', array( $this, 'try_change_thousand_separator' ) );
		add_filter( 'wc_get_price_decimal_separator', array( $this, 'try_change_decimal_separator' ) );
		add_filter( 'woocommerce_product_class', array( $this, 'find_product_class' ), 10, 4 );
		add_action( 'woocommerce_before_order_object_save', array( $this, 'before_order_save' ) );
		add_action( 'woocommerce_before_order_refund_object_save', array( $this, 'before_order_save' ), 10, 2 );
		add_action( 'woocommerce_process_shop_order_meta', array( $this, 'update_order_currency' ) );
		add_filter( 'woocommerce_get_variation_prices_hash', array( $this, 'filter_price_hash' ), 10, 3 );
		add_filter( 'przelewy24_multi_currency_admin_currency', array( $this, 'try_change_default_currency' ) );
		add_filter( 'woocommerce_reports_get_order_report_query', array( $this, 'sql_override' ), 10, 1 );
		add_filter( 'woocommerce_admin_rest_controllers', array( $this, 'update_admin_rest_controllers' ) );
	}
}
