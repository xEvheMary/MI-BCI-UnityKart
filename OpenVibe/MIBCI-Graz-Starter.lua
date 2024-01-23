
function initialize(box)

	dofile(box:get_config("${Path_Data}") .. "/plugins/stimulation/lua-stimulator-stim-codes.lua")

	number_of_trials = box:get_setting(2)
	first_class = _G[box:get_setting(3)]
	second_class = _G[box:get_setting(4)]
	baseline_duration = box:get_setting(5)
	wait_for_beep_duration = box:get_setting(6)
	wait_for_cue_duration = box:get_setting(7)
	display_cue_duration = box:get_setting(8)
	feedback_duration = box:get_setting(9)
	end_of_trial_min_duration = box:get_setting(10)
	end_of_trial_max_duration = box:get_setting(11)

end

function process(box)

	local t=0

	-- manages baseline

	box:send_stimulation(1, OVTK_StimulationId_ExperimentStart, t, 0)
	t = t + 2

	box:send_stimulation(1, OVTK_StimulationId_BaselineStart, t, 0)
	box:send_stimulation(1, OVTK_StimulationId_Beep, t, 0)
	t = t + baseline_duration

	box:send_stimulation(1, OVTK_StimulationId_BaselineStop, t, 0)
	t = t + 3

	box:sleep()

end
