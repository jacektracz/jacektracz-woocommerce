<?php
/**
 * Template for active multi currency.
 *
 * @package Przelewy24
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! isset( $value ) ) {
	throw new LogicException( 'The variable $value is not set.' );
}
if ( $value ) {
	if ( ! isset( $currency_options ) ) {
		throw new LogicException( 'The variable $currency_options is not set.' );
	}
	if ( ! isset( $report_currency ) ) {
		throw new LogicException( 'The variable $active_currency is not set.' );
	}
}

?>

<h1><?php echo esc_html( __( 'Moduł multi currency' ) ); ?></h1>

<p class="p24-info">
	Wtyczka płatności Przelewy24 posiada zintegrowany moduł do obsługi wielu walut
	w kontekście jednego sklepu. Po jego aktywacji należy przejść do zakładki
	z mnożnikami i dodać kolejne waluty.
</p>

<form method="post">
	<table>
		<tr>
			<?php $field_id = 'p24_multi_currency_active_' . wp_rand(); ?>
			<th>
				<label for="<?php echo esc_attr( $field_id ); ?>"><?php echo esc_html( __( 'Aktywować moduł multi currency' ) ); ?></label>
			</th>
			<td>
				<input type="checkbox" name="p24_multi_currency_active" id="<?php echo esc_attr( $field_id ); ?>" value="yes" <?php echo $value ? 'checked="checked"' : ''; ?> />
			</td>
		</tr>
		<?php if ( $value ) { ?>
			<tr>
				<?php $reports_field_id = 'p24_reports_currency_' . wp_rand(); ?>
				<th>
					<label for="<?php echo esc_attr( $reports_field_id ); ?>"><?php echo esc_html( __( 'Waluta do analityki (w tym dashboard)' ) ); ?></label>
				</th>
				<td>
					<select title="<?php echo esc_attr( __( 'Waluta do analityki (w tym dashboard)' ) ); ?>" name="p24_reports_currency" id="<?php echo esc_attr( $reports_field_id ); ?>">
						<?php foreach ( $currency_options as $currency_option ) : ?>
							<option value="<?php echo esc_attr( $currency_option ); ?>" <?php echo $currency_option === $report_currency ? 'selected="selected"' : ''; ?>>
								<?php echo esc_html( $currency_option ); ?>
							</option>
						<?php endforeach; ?>
					</select>
				</td>
			</tr>
		<?php } ?>
		<tr>
			<td colspan="2">
				<input type="hidden" name="p24_action_type_field" value="activate_multi_currency" />
				<?php wp_nonce_field( 'p24_action', 'p24_nonce' ); ?>
				<input type="submit" value="<?php echo esc_html( __( 'Zapisz' ) ); ?>" />
			</td>
		</tr>

	</table>
</form>
<?php
