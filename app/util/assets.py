from flask_assets import Bundle

bundles = {
    'index_js': Bundle(
        'js/index.js',
        output='gen/index.js'),
}
