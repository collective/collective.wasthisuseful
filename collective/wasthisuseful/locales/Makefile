I18NDUDE = i18ndude
PRODUCTNAME = collective.wasthisuseful
I18NDOMAIN := ${PRODUCTNAME}

default:help
	@echo "-------------------------------------------------------------------"
	@echo "Nothing to be done by default."
	@echo "-------------------------------------------------------------------"

help:
	@echo "-------------------------------------------------------------------"
	@echo "MANUAL"
	@echo "pot             : update potfile"
	@echo "sync lang=XX    : sync .po-file for language XX"
	@echo "compile lang=XX : compile .mo-file for language XX"
	@echo "-------------------------------------------------------------------"

pot:
	@echo "-------------------------------------------------------------------"
	@echo "Generating potfile..."
	${I18NDUDE} rebuild-pot --pot ${PRODUCTNAME}.pot --create ${I18NDOMAIN} ../
	@echo "-------------------------------------------------------------------"

sync:
	@echo "-------------------------------------------------------------------"
	@if [ -z $(lang) ]; \
	then echo "No language specified";\
	else echo "Syncing language $(lang)";\
	${I18NDUDE} sync --pot ${PRODUCTNAME}.pot $(lang)/LC_MESSAGES/${PRODUCTNAME}.po;\
	fi
	@echo "-------------------------------------------------------------------"

compile:
	@echo "-------------------------------------------------------------------"
	msgfmt -o $(lang)/LC_MESSAGES/${PRODUCTNAME}.mo $(lang)/LC_MESSAGES/${PRODUCTNAME}.po
	@echo "-------------------------------------------------------------------"

