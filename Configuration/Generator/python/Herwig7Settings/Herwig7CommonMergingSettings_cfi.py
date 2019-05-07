import FWCore.ParameterSet.Config as cms

herwig7CommonMergingSettingsBlock = cms.PSet(
    hw_common_merging_settings = cms.vstring(
            'read snippets/PPCollider.in', 
            'cd /Herwig/EventHandlers', 
            'library FxFx.so', 
            'create Herwig::FxFxEventHandler theLesHouchesHandler', 
            'cd /Herwig/EventHandlers', 
            'library FxFx.so', 
            'create Herwig::FxFxFileReader theLHReader', 
            'cd /Herwig/Shower', 
            'library FxFxHandler.so', 
            'create Herwig::FxFxHandler FxFxHandler', 
            'set /Herwig/Shower/FxFxHandler:ShowerModel /Herwig/Shower/ShowerModel', 
            'set /Herwig/Shower/FxFxHandler:SplittingGenerator /Herwig/Shower/SplittingGenerator', 
            'cd /Herwig/EventHandlers', 
            'create ThePEG::Cuts   /Herwig/Cuts/NoCuts', 
            'cd /Herwig/EventHandlers', 
            'insert theLesHouchesHandler:FxFxReaders[0] theLHReader', 
            'set theLesHouchesHandler:WeightOption VarNegWeight', 
            'set theLesHouchesHandler:PartonExtractor /Herwig/Partons/PPExtractor', 
            'set theLesHouchesHandler:CascadeHandler /Herwig/Shower/FxFxHandler', 
            'set theLesHouchesHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler', 
            'set theLesHouchesHandler:DecayHandler /Herwig/Decays/DecayHandler', 
            'set /Herwig/Shower/ShowerHandler:MaxPtIsMuF Yes', 
            'set /Herwig/Shower/ShowerHandler:RestrictPhasespace Yes', 
            'set /Herwig/Shower/PartnerFinder:PartnerMethod Random', 
            'set /Herwig/Shower/PartnerFinder:ScaleChoice Partner', 
            'cd /Herwig/EventHandlers', 
            'set theLHReader:AllowedToReOpen No',
            'set theLHReader:WeightWarnings    false', 
            'set theLHReader:FileName cmsgrid_final.lhe', 
            'set theLHReader:MomentumTreatment      RescaleEnergy', 
            'set theLHReader:Cuts  /Herwig/Cuts/NoCuts', 
            'cd /Herwig/Generators', 
            'set EventGenerator:EventHandler  /Herwig/EventHandlers/theLesHouchesHandler', 
            'set EventGenerator:NumberOfEvents 100000000', 
            'set EventGenerator:PrintEvent     1', 
            'set EventGenerator:MaxErrors      10000', 
            'cd /Herwig/Shower', 
            'set /Herwig/Shower/FxFxHandler:MPIHandler  /Herwig/UnderlyingEvent/MPIHandler', 
            'set /Herwig/Shower/FxFxHandler:RemDecayer  /Herwig/Partons/RemnantDecayer', 
            'set /Herwig/Shower/FxFxHandler:ShowerAlpha  AlphaQCD', 
            'set FxFxHandler:HeavyQVeto Yes', 
            'set FxFxHandler:HardProcessDetection Automatic', 
            'set FxFxHandler:ihrd        3', 
            'set FxFxHandler:njetsmax      4', 
            'set FxFxHandler:drjmin      0', 
            'cd /Herwig/Shower', 
            'set FxFxHandler:VetoIsTurnedOff VetoingIsOn', 
            'set FxFxHandler:MergeMode TreeMG5', 
            'set FxFxHandler:ETClus 20*GeV', 
            'set FxFxHandler:RClus 1.0', 
            'set FxFxHandler:EtaClusMax 5', 
            'set FxFxHandler:RClusFactor 1.5'

    )
)
