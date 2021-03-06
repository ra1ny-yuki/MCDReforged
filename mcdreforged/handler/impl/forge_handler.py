from mcdreforged.handler.impl.vanilla_handler import VanillaHandler


class ForgeHandler(VanillaHandler):
	# [18:26:03] [Server thread/INFO] [FML]: Unloading dimension 1
	# [18:26:03] [Server thread/INFO] [minecraft/DedicatedServer]: Done (9.855s)! For help, type "help" or "?"
	# [18:29:30] [Server thread/INFO] [minecraft/DedicatedServer]: <Steve> tests
	@classmethod
	def get_content_parsing_formatter(cls):
		return '[{hour:d}:{min:d}:{sec:d}] [{thread}/{logging}] [{forge_logging}]: {content}'
