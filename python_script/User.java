
		Map<String, Object> result = new HashMap<>();
		result.put("success", true);
		// change map to a json string format
		String resultJson = new ObjectMapper().writeValueAsString(result);
		
		PrintWriter out = response.getWriter();
		response.setContentType("application/json");
		response.setCharacterEncoding("UTF-8");
		out.print(resultJson);
		
		out.flush();
		